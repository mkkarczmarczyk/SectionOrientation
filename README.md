# SectionOrientation
Rotate structural member to be aligned with the adjacent planes.

Konstrukcje budowlane takie jak świetliki lub instalacje rzeźbiarskie (rys. 1) pokryte są panelami ze szkła lub innego materiału, np sklejki. 
![Zacheta_04_2(0)](https://user-images.githubusercontent.com/24354442/64923156-950b5880-d7d7-11e9-9fd0-c37c4b472b5d.png)
W wypadku gdy strukturę nośną (pręty) stanowią elementy o przekroju prostokątnym, pożądane jest obrócenie go tak,żeby był jednkowym kątem wobec obu paneli (płaszczyzn) (rys.2).
<img width="597" alt="image" src="https://user-images.githubusercontent.com/24354442/64923212-04814800-d7d8-11e9-964e-ae4c62847279.png">

Skrypt w Pythonie, na podstawie topologii prętów (belki.txt)i paneli (tri3.txt) oraz cosinusów kierunkowych prętów, tworzy plik z kątami obrotów poszczególnych prętów (beta.txt).
