import { Component, OnInit } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser'
import { ThrowStmt } from '@angular/compiler';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css'],
})
export class ProductsComponent implements OnInit {
  public showCategories: boolean;
  public showSort: boolean;
  public showloadMore:boolean;

  public categories:String[];

  constructor() { }

  ngOnInit(): void {
    this.showCategories, this.showSort,this.showloadMore= false;
     this.categories= ["Salas","Dormitorios","Comedores","Infantil"];
  }

  showCategoriesEvent(): void {
    this.showCategories = !this.showCategories;
  }

  showSortEvent(): void {
    this.showSort = !this.showSort;
  }

}
