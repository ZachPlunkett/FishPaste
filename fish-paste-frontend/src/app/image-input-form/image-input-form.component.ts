import { environment } from './../../environments/environment';
import { FlaskBackendService } from './../flask-backend.service';
import { Component, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-image-input-form',
  templateUrl: './image-input-form.component.html',
  styleUrls: ['./image-input-form.component.css']
})
export class ImageInputFormComponent implements OnInit {
  imageForUpload: File | null | undefined;
  resultPath: string | undefined;
  isLoading = false;

  constructor(private flaskBack: FlaskBackendService) { }

  ngOnInit() {
  }

  fileChosen(event: Event): void {
    const target = event.target as HTMLInputElement;
    if (target && target.files && target.files[0]) {
      this.imageForUpload = target.files[0];
    }
  }

  processImage(): void {
    if (this.imageForUpload) {
      this.isLoading = true;

      this.flaskBack.uploadImage(this.imageForUpload).subscribe(r => {
          if (r.imagePath) {
            this.resultPath = r.imagePath.replace('\\', '/');
            this.imageForUpload = null;
          }
        },
        () => {},
        () => this.isLoading = false
      );
    }
  }

  getFullImageUrl(): string {
    if (this.resultPath) { return environment.backendUrlRoot + this.resultPath; }

    return '';
  }

}
