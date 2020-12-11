import { environment } from '../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FlaskBackendService {
  backendApiRoot = environment.backendUrlRoot;

  constructor(private http: HttpClient) { }

  uploadImage(image: File): Observable<any> {
    const formData = new FormData();
    formData.append('file', image);
    return this.http.post<any>(`${this.backendApiRoot}upload`, formData);
  }
}
