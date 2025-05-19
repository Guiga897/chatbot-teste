from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionConfirmaCadastro(Action):
    def name(self) -> Text:
        return "action_confirma_cadastro"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Cadastro realizado com sucesso! ID gerado: #12345")
        return []

class ActionRegistrarOcorrencia(Action):
    def name(self) -> Text:
        return "action_registrar_ocorrencia"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Ocorrência registrada com sucesso na ficha do aluno.")
        return []