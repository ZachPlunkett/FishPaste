/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { FlaskBackendService } from './flask-backend.service';

describe('Service: FlaskBackendService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [FlaskBackendService]
    });
  });

  it('should ...', inject([FlaskBackendService], (service: FlaskBackendService) => {
    expect(service).toBeTruthy();
  }));
});
