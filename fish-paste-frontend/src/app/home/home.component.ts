import { animate, state, style, transition, trigger } from '@angular/animations';
import { AfterViewInit, Component, OnInit } from '@angular/core';
import { interval } from 'rxjs';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  animations: [
    trigger('slideIn', [
      state('false', style({
        transform: 'translateX(-1000px)'
      })),
      state('true', style({
        transform: 'translateX(0)'
      })),
      transition('true <=> false', animate('200ms ease-in-out'))
    ])
  ]
})
export class HomeComponent implements OnInit, AfterViewInit {
  welcomeCardVisible = false;
  constructor() { }

  ngOnInit() {
  }

  ngAfterViewInit() {
    setTimeout(() => this.welcomeCardVisible = true, 100);
  }

}
