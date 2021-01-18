import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './components/root/app.component';

import { HeaderComponent } from './components/common/header/header.component'
import { FooterComponent } from './components/common/footer/footer.component'
import { WhatsappComponent } from './components/common/whatsapp/whatsapp.component'
import { Routes, RouterModule } from '@angular/router'; // CLI imports router

//Pages
import { HomeComponent } from "./components/home/home/home.component";
import { ProductsComponent } from "./components/products/products/products.component";
import { ServicesComponent } from "./components/services/services/services.component";
import { AboutComponent } from "./components/about/about/about.component";
import { ContactComponent } from "./components/contact/contact/contact.component";
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';


const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'products', component: ProductsComponent },
  { path: 'services', component: ServicesComponent },
  { path: 'about', component: AboutComponent },
  { path: 'contact', component: ContactComponent },
];

const otherComponents=[HomeComponent,ProductsComponent,ServicesComponent,AboutComponent,ContactComponent];


@NgModule({
  declarations: [
    AppComponent, HeaderComponent, FooterComponent, WhatsappComponent,...otherComponents
  ],

  imports: [
    BrowserModule, RouterModule.forRoot(routes), NgbModule, BrowserAnimationsModule
  ],
  exports: [RouterModule],
  providers: [],
  bootstrap: [AppComponent],
//schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppModule { }