import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VisualisationnianticComponent } from './visualisationniantic.component';

describe('VisualisationnianticComponent', () => {
  let component: VisualisationnianticComponent;
  let fixture: ComponentFixture<VisualisationnianticComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VisualisationnianticComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VisualisationnianticComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
