import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-whatsapp',
  templateUrl: './whatsapp.component.html',
  styleUrls: ['./whatsapp.component.css']
})
export class WhatsappComponent implements OnInit {

  public WhatsappChat:boolean;

  constructor() { }

  ngOnInit(): void {
    this.WhatsappChat=false;
  }

  WhatsappHidden():void{
    this.WhatsappChat=!this.WhatsappChat;
  }
}
