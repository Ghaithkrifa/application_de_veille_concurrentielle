import { rates } from './../../../services/competitor-posts.service';
import { CompetitorPostsService } from 'src/app/services/competitor-posts.service';
import { Component, OnInit } from '@angular/core';
import { CompetitorService } from 'src/app/services/competitor.service';
import { Chart } from 'chart.js';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-visualisationgather',
  templateUrl: './visualisationgather.component.html',
  styleUrls: ['./visualisationgather.component.css'],
})
export class VisualisationgatherComponent implements OnInit {
  page: string = ' Daily page views per visitors';
  time: string = ' Daily time on sites';
  bounce: string = 'Bounce rates';

  showMe: string = 'linkedin';

  toogletag() {
    this.showMe = 'linkedin';
    this.myChart.destroy();
    this.searchForm.reset();
  }
  toogletag1() {
    this.showMe = 'youtube';
    this.myChart.destroy();
    this.searchForm1.reset();
  }
  positive: number[] = [];
  negative: number[] = [];
  sentchart: any;
  sentchart1: any;
  apireviwes: any;
  apiyout: any;
  page_viewsvisitors: string[] = [];
  time_on_sites: string[] = [];
  bounce_rates: string[] = [];
  apialexa: any;
  chart1: any;
  myChart: any;
  myChart1: any;
  chartyoutube: any;
  chartyoutube1: any;
  chartyoutube2: any;
  chart: any;
  pychart: any;
  pychart1: any;
  pychart2: any;
  linchart: any;
  linchart1: any;
  lab: string = "Nombre d'employés ";
  lab1: string = "Nombre d'abonnés ";

  lab_yout1: string = 'subscriberCount';
  lab_yout2: string = 'videoCount';
  competitorName1: string = 'talan';
  competitorName: string = 'gather';
  dates: string[] = [];
  dates1: string[] = [];
  nb_rates: number[] = [];
  nbratesyoutube: number[] = [];
  nbratesyoutube1: number[] = [];
  nb_rates1: number[] = [];
  apiCompititors: any;
  competitor_rates: any;
  competitor_rates1: any;
  employes: number[] = [];
  nb_abonnee: number[] = [];
  subscriberCount: number[] = [];
  videoCount: number[] = [];
  viewCount: number[] = [];

  searchForm = new FormGroup({
    periode: new FormControl(),
    engagementRate: new FormControl(),
    type: new FormControl(),
  });
  searchForm1 = new FormGroup({
    periode1: new FormControl(),
    engagementRate1: new FormControl(),
  });

  constructor(
    private competitorService: CompetitorService,
    private CompetitorPostsService: CompetitorPostsService
  ) {}

  ngOnInit(): void {
    this.sentchart = document.getElementById('sentimentchart');
    this.sentchart1 = document.getElementById('sentimentchart1');

    this.chart = document.getElementById('abonnee_chart');
    this.chart1 = document.getElementById('employee_chart');
    this.linchart = document.getElementById('ratechart');
    this.linchart1 = document.getElementById('rateyoutubechart');
    this.pychart = document.getElementById('piechart');
    this.pychart1 = document.getElementById('piechart1');
    this.pychart2 = document.getElementById('piechart2');
    this.chartyoutube1 = document.getElementById('videochart');
    this.chartyoutube2 = document.getElementById('subscribechart');

    this.getdonnegeneral();
    this.getalexa();
    this.getyoutubechanel();
    this.getrev();
  }

  searchyoutube() {
    const { periode1, engagementRate1 } = this.searchForm1.value;
    console.table(periode1, engagementRate1);
    this.CompetitorPostsService.fetchrateyoutube(
      this.competitorName,
      periode1,
      engagementRate1
    ).subscribe(
      (res1: rates) => {
        this.competitor_rates1 = res1;
        console.log("ghfjgkhgfh",this.competitor_rates1);
        this.dates1 = this.competitor_rates1[0];
        this.nbratesyoutube = this.competitor_rates1[1];
        this.nbratesyoutube1 = this.competitor_rates1[2];
        if (this.dates1.length == 0) {
          alert('No data available');
          this.myChart.destroy();
        }
        else{
        this.loadChart(this.dates1, this.nbratesyoutube, this.nbratesyoutube1);
      }},
      (err) => {
        console.log(err);
      }
    );
  }

  searchPosts() {
    const { periode, engagementRate, type } = this.searchForm.value;

    this.CompetitorPostsService.fetchrate(
      this.competitorName,
      type,
      periode,
      engagementRate
    ).subscribe(
      (res: rates) => {
        this.competitor_rates = res;
        this.dates = [];
        this.nb_rates = [];
        this.nb_rates1 = [];
        this.dates = this.competitor_rates[0];
        this.nb_rates = this.competitor_rates[1];
        this.nb_rates1 = this.competitor_rates[2];
        console.log('hhhh', this.dates);
        if (this.dates.length == 0) {
          alert('No data available');
          this.myChart.destroy();
        } else {
          this.loadChart(this.dates, this.nb_rates, this.nb_rates1);
        }
      },
      (err) => {
        console.log(err);
      }
    );
  }
  loadChart(dat: string[], rat1: number[], rat2: number[]): void {
    if (this.myChart) this.myChart.destroy();
    this.myChart = new Chart(this.linchart, {
      type: 'line',
      data: {
        datasets: [
          {
            data: rat1,
            label: 'gather',
            tension: 0.2,
          },
          {
            data: rat2,
            label: 'talan',
            tension: 0.2,
          },
        ],
        labels: dat,
      },
    });
  }

  getalexa(): void {
    this.competitorService.getalexa().subscribe((res) => {
      this.apialexa = res;
      for (let pas = 0; pas < this.apialexa.length; pas++) {
        if (
          this.apialexa[pas]['competitor'] == 'gather' ||
          this.apialexa[pas]['competitor'] == 'talan'
        ) {
          this.page_viewsvisitors.push(
            this.apialexa[pas]['daily_page_views_per_visitors']
          );
          this.time_on_sites.push(this.apialexa[pas]['daily_time_on_sites']);
          this.bounce_rates.push(this.apialexa[pas]['bounce_rates']);
        }
      }

      this.pichart(this.page_viewsvisitors, this.pychart, this.page);
      this.pichart(this.time_on_sites, this.pychart1, this.time);
      this.pichart(this.bounce_rates, this.pychart2, this.bounce);
    });
  }
  pichart(page_views: string[], chartt: any, lab: string) {
    new Chart(chartt, {
      type: 'doughnut',

      data: {
        datasets: [
          {
            data: page_views,

            backgroundColor: [
              'rgba(13, 50, 220, 0.8)',
              'rgba(118, 236, 237, 0.8)',
            ],
          },
        ],
        labels: ['talan', 'gather'],
      },
      options: {
        plugins: {
          title: {
            display: true,
            text: lab,
          },
        },
      },
    });
  }

  getdonnegeneral(): void {
    this.competitorService.getcompetitors().subscribe((res) => {
      this.apiCompititors = res;
      console.log(this.apiCompititors);

      for (let pas = 0; pas < this.apiCompititors.length; pas++) {
        if (
          this.apiCompititors[pas]['competitor'] == 'gather' ||
          this.apiCompititors[pas]['competitor'] == 'talan'
        ) {
          this.employes.push(this.apiCompititors[pas]['employees']);
          this.nb_abonnee.push(this.apiCompititors[pas]['subscribers']);
        }
      }
      this.barChart(
        this.chart,
        this.nb_abonnee[0],
        this.nb_abonnee[1],
        this.lab1
      );
      this.barChart(this.chart1, this.employes[0], this.employes[1], this.lab);
    });
  }
  barChart(chartt: any, nb_abonnee: Number, nb_abonnee1: any, lb: String) {
    new Chart(chartt, {
      type: 'bar',
      data: {
        datasets: [
          {
            data: [nb_abonnee],
            label: 'talan',
            backgroundColor: 'rgba(13, 50, 220, 0.8)',
            maxBarThickness: 35,
            minBarLength: 10,
          },
          {
            data: [nb_abonnee1],
            label: 'gather',
            backgroundColor: 'rgba(118, 236, 237, 0.8)',
            maxBarThickness: 35,
            minBarLength: 10,
          },
        ],
        labels: [lb],
      },
    });
  }

  getyoutubechanel() {
    this.competitorService.getyoutubechaine().subscribe((res) => {
      this.apiyout = res;
      for (let pas = 0; pas < this.apiyout.length; pas++) {
        if (
          this.apiyout[pas]['competitor'] == 'gather' ||
          this.apiyout[pas]['competitor'] == 'talan'
        ) {
          this.subscriberCount.push(this.apiyout[pas]['subscriberCount']);
          this.videoCount.push(this.apiyout[pas]['videoCount']);
          this.viewCount.push(this.apiyout[pas]['viewCount']);
        }
      }

      this.barChart(
        this.chartyoutube2,
        this.subscriberCount[0],
        this.subscriberCount[1],
        this.lab_yout1
      );
      this.barChart(
        this.chartyoutube1,
        this.videoCount[0],
        this.videoCount[1],
        this.lab_yout2
      );
    });
  }
  getrev() {
    this.competitorService.getreviws().subscribe((res) => {
      this.apireviwes = res;
      for (let pas = 0; pas < this.apireviwes.length; pas++) {
        if (
          this.apireviwes[pas]['competitor'] == 'gather' ||
          this.apireviwes[pas]['competitor'] == 'talan'
        ) {
          this.positive.push(this.apireviwes[pas]['postive']);
          this.negative.push(this.apireviwes[pas]['negative']);
        }
      }
      this.pieChartt(
        this.sentchart,
        this.positive[0],
        this.negative[0],
        this.competitorName1
      );
      this.pieChartt(
        this.sentchart1,
        this.positive[1],
        this.negative[1],
        this.competitorName
      );
    });
  }

  pieChartt(
    chartt: any,
    nb_abonnee: Number,
    nb_abonnee1: Number,
    competitor: string
  ) {
    new Chart(chartt, {
      type: 'pie',
      data: {
        datasets: [
          {
            data: [nb_abonnee, nb_abonnee1],

            backgroundColor: [
              'rgba(118, 236, 237, 0.8)',
              'rgba(13, 50, 220, 0.8)',
            ],
          },
        ],
        labels: ['positive', 'negative'],
      },
      options: {
        plugins: {
          title: {
            display: true,
            text: competitor,
          },
        },
      },
    });
  }
}