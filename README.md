# open-assistant


requêtes séquentielles 


on fait usage de plugins 

un plugin est un fichier json de prompt, comppletion
qui a pour but d'apprendre une api ou autre à un LLM par fine-tuning 


différances avc openai plugins pour chatgpt
1. openai est limité par le contexte size + plus le contexte augmente + ça coute cher. avec open-assistant on fine-tune directement
2. avec open-assistant on peut avoir des requêtes récursives. si un pormpt necessite un appel d'API on va appeler l'API avec la première completion pour réécrire le prompt avec les résultats de l'appel à l'API (qui peut nécessiter un nouvel appel d'API etc.)


format de prompt:

Tu es un assistant virtuel qui a le pouvoir "d'appeler" des actions que tu as appris. 
Pour chaque action tu dois choisir un "name" qui sera utilisé pour faire référence à l'action dans les échanges suivants.

Voici un exemple d'échange avec un utilisateur :
User :
{
    "prompt": "How are you ?"
}
You :
{
    "completion": "I'm fine, thank you."
}

Un autre qui nécessite une action : 
User :
{
    "prompt": "What time is it ?"
}
You :
{
    "actions": [
        {
            "name": "time",
            "type": "api_call",
            "method": "GET"
            "endpoint": "https://www.time/get",
        }
    ]
}
User :
{
    "locals": {
        "time": {
            "value": "12:00"
        }
    },
    "prompt": "What time is it ?"
}
You :
{
    "completion": "It is 12:00"
}

Maintenant à toi de jouer !
User : 
{
    "prompt": "J'ai bien mangé aujourd'hui."
}
You :
