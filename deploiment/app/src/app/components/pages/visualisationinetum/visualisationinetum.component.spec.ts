import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisualisationinetumComponent } from './visualisationinetum.component';

describe('VisualisationinetumComponent', () => {
  let component: VisualisationinetumComponent;
  let fixture: ComponentFixture<VisualisationinetumComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VisualisationinetumComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VisualisationinetumComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
