import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-image-input-form',
  templateUrl: './image-input-form.component.html',
  styleUrls: ['./image-input-form.component.css']
})
export class ImageInputFormComponent implements OnInit {
  imageForUpload!: File;
  constructor() { }

  ngOnInit() {
  }

  fileChosen(event: Event): void {
    const target = event.target as HTMLInputElement;
    if (target && target.files && target.files[0]) {
      this.imageForUpload = target.files[0];
    }
  }

  processImage(): void {
    // todo: create image upload service and send request
  }

}
