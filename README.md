# open-assistant


requêtes séquentielles 


on fait usage de plugins 

un plugin est un fichier json de prompt, comppletion
qui a pour but d'apprendre une api ou autre à un LLM par fine-tuning 


différances avc openai plugins pour chatgpt
> openai est limité par le contexte size + plus le contexte augmente + ça coute cher. avec open-assistant on fine-tune directement
> avec open-assistant on peut avoir des requêtes récursives. si un pormpt necessite un appel d'API on va appeler l'API avec la première completion pour réécrire le prompt avec les résultats de l'appel à l'API (qui peut nécessiter un nouvel appel d'API etc.)