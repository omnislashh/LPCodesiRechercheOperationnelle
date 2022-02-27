## Tests pour le sujet de recherche operationnelle
***
Choix de python 3  
Modules: orTools (GoogleSuite)  
Ressources: https://developers.google.com/optimization/assignment/assignment_example  

main file: fonction-eval.py

1. Travail dans une seule fonction main() dans un premier tps
2. ToDo: Créer les fonctions Eval(O) + Glouton séparée, et la fonction main devrait appeler ces sous-fonctions
3. Le lecteur de fichier récupère un seul fichier "en dur" pour l'instant
4. ToDo: tester avec un autre jeu de résultats
5. La fonction glouton n'implémente pas la même condition que Eval(0)
6. Le prix limite est défini arbitrairement (fn) mais ne correspond pas forcément au prix d'ouverture d'un fournisseur
7. Le poids fait référence au prix
8. Une proposition avec le prix opti des fournisseurs optimum est proposé en commentaire :  
```# poids_max = sum(word_dict.values())```
9. Pour glpk:  
https://martin-thoma.com/how-to-use-glpk/#assignment-problem