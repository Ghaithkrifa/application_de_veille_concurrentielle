import {
  CompetitorPostsService,
  Likes,
} from 'src/app/services/competitor-posts.service';
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';
import { CompetitorService } from 'src/app/services/competitor.service';
@Component({
  selector: 'app-a-regarder',
  templateUrl: './a-regarder.component.html',
  styleUrls: ['./a-regarder.component.css'],
})
export class ARegarderComponent implements OnInit {
  //apiLikes: Observable<Likes[]>;
  //likespost: Likes[];

  constructor(
    private competitorService: CompetitorService,
    private competitorPostsService: CompetitorPostsService,
    private router: Router
  ) {
    //this.apiLikes = this.competitorPostsService.getpostsliked();
  }
  likespost: any;
  comm: any;
  ngOnInit(): void {
    this.listlikesposts();
    this.get_opinons();
  }

  listlikesposts(): void {
    console.log('hello');
    this.competitorPostsService.getpostsliked().subscribe((res) => {
      this.likespost = res;
      console.log('hello', this.likespost);
    });
  }
  get_opinons() {
    this.competitorService.getopinions().subscribe((res) => {
      this.comm = res;
    });
  }

  deletelikes(id: string) {
    if (confirm('Are your sure you want to delete this post?')) {
      this.competitorPostsService.deletePosts(id).subscribe(
        () => {
          this.ngOnInit();
        },
        () => {
          alert('Error');
        }
      );
    }
  }
}
