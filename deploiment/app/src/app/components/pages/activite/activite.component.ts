import { Competitor, opinion } from './../../../services/competitor.service';
import { Observable } from 'rxjs';
import { CompetitorPost } from './../../../services/competitor-posts.service';
import { AuthService, AuthUser } from 'src/app/services/auth.service';
import { Component, OnInit } from '@angular/core';
import { CompetitorService } from 'src/app/services/competitor.service';
import { CompetitorPostsService } from 'src/app/services/competitor-posts.service';
import {
  FormGroup,
  FormControl,
  Validators,
  FormBuilder,
} from '@angular/forms';
@Component({
  selector: 'app-activite',
  templateUrl: './activite.component.html',
  styleUrls: ['./activite.component.css'],
})
export class ActiviteComponent implements OnInit {
  compteur: number = 0;
  user?: AuthUser;
  posts: any = 0;
  comm: any;
  jaime: any;
  nbrate: number = 0;
  commmentaire: any;
  //CompetitorPost[] = [];
  comment: string = '';
  apiCompititors: Observable<Competitor[]>;
  searchForm = new FormGroup({
    start: new FormControl(null, [Validators.required]),
    end: new FormControl(null, [Validators.required]),
    competitorName: new FormControl(),
    type: new FormControl(),
    filter: new FormControl(),
  });

  ghaithForm = this.formBuilder.group({
    comment: null,
  });

 

  constructor(
    private competitorService: CompetitorService,
    private CompetitorPostsService: CompetitorPostsService,
    private formBuilder: FormBuilder,
    private authService: AuthService
  ) {
    this.user = this.authService.user;
    console.log('aaaaaaaaaaa', this.user?._id);
    this.apiCompititors = this.competitorService.getcompetitors();
  }

  ngOnInit(): void {
    this.get_opinons();
    this.get_rates();
  }

 
  toogle(link: string) {
    this.CompetitorPostsService.sendlike(link).subscribe(
      () => {
        this.ngOnInit();
      },
      () => {
        console.log('nonsucsess');
      }
    );
  }
  
deleteopin(link: string, comm: string, name: string) {
    if (confirm('Are your sure you want to delete this comments?'))
      this.CompetitorPostsService.deleteopinion(link, comm, name).subscribe(
        () => {
          this.ngOnInit();
        },
        () => {
          alert('Error');
        }
      );
  }
  addcomments(link: string) {
    this.comment = this.ghaithForm.value;
    this.compteur = 0;
    for (let pas = 0; pas < this.ghaithForm.value['comment'].length; pas++) {
      if (this.ghaithForm.value['comment'][pas] == ' ') {
        ++this.compteur;
      }
    }

    if(this.ghaithForm.value['comment'] != null &&
    this.ghaithForm.value['comment'].length != this.compteur){
      this.CompetitorPostsService.addopinion(link, this.comment).subscribe(
    
        () => {
          this.ghaithForm.reset()
          this.ghaithForm.value
          this.ngOnInit();
          
        },
        () => {
          console.log('failed');
        }
      );
  
      }
    }
    
 
  searchPosts() {
    const { start, end, competitorName, type, filter } = this.searchForm.value;
    console.table({ start, end, competitorName, type });
    if (this.searchForm.valid) {
      this.CompetitorPostsService.fetchPosts(
        competitorName,
        type,
        start,
        end,
        filter
      ).subscribe(
        (data: CompetitorPost[]) => {
          //console.log(data);
          this.posts = data;
          console.log('qqqqq', this.posts[0]._id.$oid);
        },
        (err) => {
          console.log(err);
        }
      );
    }
  }
  name: any = Array();
  valeur: any = Array();
  get_opinons() {
    this.competitorService.getopinions().subscribe((res) => {
      this.comm = res;
      console.log('abed9ader', this.comm[0].liste[6].ref.$oid);
      if (this.comm[0].liste[6].ref.$oid == this.user?._id.$oid) {
        console.log('true');
      } else {
        console.log('false');
      }
    });
  }
  get_rates() {
    this.competitorService.getjaime().subscribe((res) => {
      this.jaime = res;
      console.log('aaaaaqqq', this.jaime[0].users[0].$oid);
    });
  }

  sendRegarder(link: string, id: string) {
    this.CompetitorPostsService.verifpost(id).subscribe(
      () => {
        alert('Post already exist');
      },
      () => {
        this.CompetitorPostsService.regarderPost(link).subscribe(
          () => {
            alert('Post added to "A regarder plus tard"');
          },
          () => {
            alert('Error');
          }
        );
      }
    );
  }
}
