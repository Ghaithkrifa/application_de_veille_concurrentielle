import { Observable } from 'rxjs';
import { API_ENDPOINT } from './configs';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

export interface Competitor {
  link_Site_web: string;
  Secteur: string;
  Siege_social: string;
  date_fondation: string;
  Specialisations: string;
  employes: string;
  nb_abonnee: string;
  competitor: string;
  link_logo: string;
  _id: any;
}
export interface reviws {
  competitor: string;
  positive: any;
  negative: any;
}
export interface alex {
  competitor: string;
  daily_page_views_per_visitors: string;
  daily_time_on_sites: string;
  bounce_rates: string;
}
export interface opinion {
  liste: [];
  post: any;
  _id: any;
}
export interface jaime {
  rate: number;
  post: any;
  _id: any;
}
export interface youtubechannel {
  competitor: string;
  subscriberCount: string;
  videoCount: number;
  viewCount: number;
}

@Injectable({
  providedIn: 'root',
})
export class CompetitorService {
  constructor(private http: HttpClient) {}
  getcompetitors() {
    return this.http.get<Competitor[]>(`${API_ENDPOINT}/competit`);
  }

  getreviws() {
    return this.http.get<reviws[]>(`${API_ENDPOINT}/reviws`);
  }
  getalexa() {
    return this.http.get<alex[]>(`${API_ENDPOINT}/alxa`);
  }
  getopinions() {
    return this.http.get<opinion[]>(`${API_ENDPOINT}/getopinion`);
  }
  getjaime() {
    return this.http.get<jaime[]>(`${API_ENDPOINT}/getrates`);
  }
  getyoutubechaine() {
    return this.http.get<youtubechannel[]>(`${API_ENDPOINT}/youtubchannel`);
  }
}
