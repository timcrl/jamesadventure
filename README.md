# JamesAdventure

Ce jeu à été crée dans le cadre d'un projet scolaire.

Pour lancer le jeu, il vous suffit d'executer avec python le fichier new-menu.py. Il est néssésaire d'avoir préalablement installé le module pygame.

James est un scientifique du futur. Il a découvert des portails pour voyager dans le temps. Malheureusement, il s'est retrouvé au temps des dinosaures. Il doit désormais traverser les époques et passer de portail en portail pour rejoindre son laboratoire.

Chaque niveau correspond à une époque. Le but de chaque niveau est donc de rejoindre le portail intertemporel pour débloquer le niveau suivant.

Dans les niveaux, il existe plusieurs types d'élements :

-Les blocs plateformes sont des blocs sur lesquels James peut se déplacer

-Les blocs invisibles, qui sont invilibles et qui agissent comme des plateformes

-Les blocs piègés, qui ont l'apparence d'une plateforme mais sur lesquels James ne peut pas se déplacer

-Les épines, qui tuent James à tout contact

-Les étoiles, que James peut ramasser. Elles permettent d'obtenir un bonus de score.

James peut se déplacer à droite et à gauche en utilisant les flèches ou les touches Q et D. Il peut sauter grâce à la flèche haut ou la touche Z, et il peut lancer une boule de feu grâce à la touche ESPACE.

Le score est inversement proportionnel au temps mis pour finir le niveau. En bref, plus le temps mis pour finir le niveau est long, plus le score est bas. Par ailleurs, chaque étoile rapporte un bonus de 150 points. Si James meurt sans finir le niveau, le score est de 0.

Attention, à cause d'un bug encore non résolu, il est néssésaire de fermer le menu du jeu après chaque niveau réussi, ou pour changer de niveau.

Il est possible de réinitialiser le jeu en inscrivant les 6 lignes suivantes dans le fichier interface.txt :

```
0
0
0
0
ON
ON
```
