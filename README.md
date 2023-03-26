# open-assistant


requêtes séquentielles 


on fait usage de plugins 

un plugin est un fichier json de prompt, comppletion
qui a pour but d'apprendre une api ou autre à un LLM par fine-tuning 


différances avc openai plugins pour chatgpt
1. openai est limité par le contexte size + plus le contexte augmente + ça coute cher. avec open-assistant on fine-tune directement
2. avec open-assistant on peut avoir des requêtes récursives. si un pormpt necessite un appel d'API on va appeler l'API avec la première completion pour réécrire le prompt avec les résultats de l'appel à l'API (qui peut nécessiter un nouvel appel d'API etc.)
3. avec fine-tuning on peut apprendre des choses plus vastes que des endpoints api, par exemple des documents etc donc on peut rajouter des connaissances 
4. contrairement au text embedding, de 1 on ne stock aucune donnée de 2 on n'a pas de soucis de taille de db trop grande de 3 lassistant trouve les "rapports" plus efficacement
5. on peut rajouter des connaissances dans un domaine déjà apres par exemple si il y a un plugin lol ba chaque patch on rajoute de nouvelles donnéeset contrairement aux embeddings on peut demander des données d'un patch précis etc alors que avc embedding ce sera pas forcément trouvé les bonnes connaissances + les embeddings rajoutent du context size
6. avc fine tune on perd argent debut pck c'est cher mais à la longue vu qu'on a des plus court prompt size ça revient moins cher
7. les créateurs de plugins auront un moyen perenne de gagner de l'argent: avc les updates par exemple un plugin Le Monde qui va proposer aux finetune tous les articles du monde et qui s'update chaque jour avc les nouveaux articles


format d'action
{
    "endpoint": "http://localhost:5000",
    "method": "POST",
    "body": {
        "name": "nom",
        "age": 20
    }
}