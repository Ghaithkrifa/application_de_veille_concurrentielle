import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisualisationgatherComponent } from './visualisationgather.component';

describe('VisualisationgatherComponent', () => {
  let component: VisualisationgatherComponent;
  let fixture: ComponentFixture<VisualisationgatherComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VisualisationgatherComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VisualisationgatherComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
