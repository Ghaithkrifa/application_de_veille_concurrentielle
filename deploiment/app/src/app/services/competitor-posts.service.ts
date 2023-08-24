import { Observable } from 'rxjs';
import { AuthService } from 'src/app/services/auth.service';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { API_ENDPOINT } from './configs';

export interface CompetitorPost {
  poste_date: Date;
  post_text: string;
  nb_jaime: number;
  nb_commantaire: number;
  nb_partage: number;
  post_link: string;
  type: string;
  nom_concurent: string;
  _id: any;
}
export interface rates {
  date: [];
  nb_rate: [];
  nb_rate1: [];
}
export interface Likes {
  post_link: string;
  post_text: string;
  type: string;
}
export interface dashboard {
  _id: any;
  nombrejaime: number;
  poste_date: Date;
  nom_concurent: string;
}

@Injectable({
  providedIn: 'root',
})
export class CompetitorPostsService {
  constructor(private http: HttpClient, private authService: AuthService) {}
  getpostsliked() {
    return this.http.get<Likes[]>(
      `${API_ENDPOINT}/likeposts`,
      this.authService.getAuthHeaders()
    );
  }

  fetchPosts(
    nom_concurent: string,
    type: string,
    start_date: Date,
    end_date: Date,
    filtrage: string
  ) {
    console.log('ghaith', start_date);
    return this.http.get<CompetitorPost[]>(
      `${API_ENDPOINT}/compt/${type}/${start_date
        .toJSON()
        .slice(0, 10)}/${end_date
        .toJSON()
        .slice(0, 10)}/${nom_concurent}/${filtrage}`
    );
  }
  fetchrate(
    nom_concurent: string,
    type_: string,
    periode: string,
    rate: string
  ) {
    return this.http.get<rates>(
      `${API_ENDPOINT}/nb/${nom_concurent}/${periode}/${type_}/${rate}`
    );
  }
  fetchrateyoutube(nom_concurent: string, periode: string, rate: string) {
    return this.http.get<rates>(
      `${API_ENDPOINT}/nn/${nom_concurent}/${periode}/${rate}`
    );
  }

  fetchdashbord() {
    return this.http.get<dashboard[]>(`${API_ENDPOINT}/dashboard`);
  }

  /* fetchdashboarding(
    nom_concurent: string,
    type: string,
    start_date: Date,
    end_date: Date
  ) {
    return this.http.get<CompetitorPost[]>(
      `${API_ENDPOINT}/dashboard/${type}/${start_date
        .toJSON()
        .slice(0, 10)}/${end_date.toJSON().slice(0, 10)}/${nom_concurent}`
    );
  } */
  //, rate: number
  sendlike(post_link: string) {
    return this.http.put(
      `${API_ENDPOINT}/rate`,
      {
        post_link: post_link,
      },
      this.authService.getAuthHeaders()
    );
  }
  deleteopinion(post_link: string, comments1: string, nom: string) {
    return this.http.put(`${API_ENDPOINT}/deleteopinion`, {
      post_link,
      comments1,
      nom,
    });
  }

  regarderPost(link: string) {
    console.log('hello service ', link);
    return this.http.post(
      `${API_ENDPOINT}/regarder`,
      {
        post_link: link,
      },
      this.authService.getAuthHeaders()
    );
  }
  addopinion(link: string, comment: string) {
    return this.http.put(
      `${API_ENDPOINT}/opinion`,
      { post_link: link, comments1: comment },

      this.authService.getAuthHeaders()
    );
  }

  verifpost(id: string) {
    return this.http.get(
      `${API_ENDPOINT}/verif/${id}`,
      this.authService.getAuthHeaders()
    );
  }

  deletePosts(id: string) {
    return this.http.delete(`${API_ENDPOINT}/deletePostlike/${id}`);
  }
}
