
<!-- Project basic information  -->
[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br>
<p align = "center">

  <a href="http://ec2-54-144-134-190.compute-1.amazonaws.com:8050/">
    <img src="images/buencafe_icon_1.png" alt="Logo" width="250" height="100">
  </a>


  <h3 align="center">Buencafé Dashboard</h3>

  <p align="center">
    Dashboard for Buencafé
    <br />
    <br />
    <a href="http://ec2-54-144-134-190.compute-1.amazonaws.com:8050/apps/home">View Demo</a>
    ·
    <a href="https://github.com/nestorcalvo/Buencafe_dashboard/issues">Report Bug</a>
    ·
    <a href="https://github.com/nestorcalvo/Buencafe_dashboard/issues">Request Feature</a>
  </p>
</p>
<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot1]](http://ec2-54-144-134-190.compute-1.amazonaws.com:8050/apps/home)
[![Product Name Screen Shot][product-screenshot2]](http://ec2-54-144-134-190.compute-1.amazonaws.com:8050/)
[![Product Name Screen Shot][product-screenshot3]](http://ec2-54-144-134-190.compute-1.amazonaws.com:8050/apps/steam)
[![Product Name Screen Shot][product-screenshot4]](http://ec2-54-144-134-190.compute-1.amazonaws.com:8050/apps/efficiency)


Buencafé is one of the main worldwide providers of soluble coffee of outstanding quality that belongs to the Federación Nacional de Cafeteros de Colombia (FNC). 
It produces lyophilized coffee, roasted coffee, coffee extract and coffee oil.

## Notebooks
Los notebooks se encuentran con nombres que describan la funcion que cumplen y se dividieron las partes del proceso mas importantes en diferentes notebooks.
<ul>
  <li>preprocesing.ipynb: Notebook creado para realizar la limpieza de datos, se eliminan datos atipicos y se realiza graficas en diferentes rangos de tiempo</li>
  <li>impute_data.ipynb: Notebook creado para solucionar los multiples problemas que ocacionaban los datos atipicos, se aplicaron tecnicas para poder corregirlos</li>
  <li>impute_data.ipynb: Notebook creado para solucionar los multiples problemas que ocacionaban los datos atipicos, se aplicaron tecnicas para poder corregirlos</li>
  <li>calculate_variables.ipynb: Notebook usado para realizar el proceso del calculo de la variable principal del proceso que es la eficiencia</li>
  <li>Model.ipynb: Notebook donde se crearon y se evaluaron los multiples modelos estadisticos para la solución del problema/li>
</ul>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

List of things you need to use the software and how to install them.
* python libraries
  ```sh
  pip install -r requirements.txt
  ```
### Run the web application

The main file is index.py, to run the application in the localhost.
* run command
  ```sh
  python index.py
  ```
<!-- CONTACT -->
## Contact

Nestor Calvo - nestorcalvoa@gmail.com

Luis Fernando Rico - luisf.ricoo@gmail.com

Ana María Gómez - anamago3@gmail.com

Maryelin Del Valle Pérez - perez.c.maryelin@gmail.com

Juan Pablo Suárez - juan.suarezr@udea.edu.co

Jorge Hernán López - jhlopezm2@gmail.com


Project Link: [https://github.com/nestorcalvo/Buencafe_dashboard](https://github.com/nestorcalvo/Buencafe_dashboard)

<!-- Links to badges (template, need repo in public) -->
[contributors-shield]: https://img.shields.io/github/contributors-anon/nestorcalvo/Buencafe_dashboard
[contributors-url]: https://github.com/nestorcalvo/Buencafe_dashboard/graphs/contributors

[issues-url]: https://github.com/nestorcalvo/Buencafe_dashboard/issues
[issues-shield]: https://img.shields.io/github/issues/nestorcalvo/Buencafe_dashboard

[license-shield]: https://img.shields.io/github/license/nestorcalvo/Buencafe_dashboard
[license-url]: https://github.com/nestorcalvo/Buencafe_dashboard/blob/master/LICENSE.txt
[product-screenshot1]: assets/images/Home_page_1.png
[product-screenshot2]: assets/images/Home_page_2.png
[product-screenshot3]: images/steam_capture.PNG
[product-screenshot4]: images/efficiency_capture.PNG
