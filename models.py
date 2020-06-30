from django.db import models
from django.utils.timezone import utc
from multiselectfield import MultiSelectField
from django.forms import ModelForm


Sintomases = (
            ('Fie', 'Fiebre'), ('ToS', 'Tos seca'), ('Can', 'Cansancio'), ('MoD','Molestias y Dolores'), ('Gar', 'Dolor de Garganta'), ('Diar', 'Diarrea'),  ('Conj','Conjuntivitis'), ('DC','Dolores de cabeza'), ('Per','Pérdida del olfato o del gusto'), ('PerC','Erupciones cutáneas o pérdida del color en extremidades'), ('Resp', 'Insuficiencia Respiratorias'),('Dif','Dificultad para respirar o sensación de falta de aire'), ('DolPe', 'Dolor o presión en el pecho'), ('Inc','Incapacidad para hablar o moverse')
            )
      

class registros(models.Model):
    dia = models.DateTimeField()
    covid = models.CharField(max_length=20)
    sintomas = MultiSelectField(choices=Sintomases)

    def publish(self):
        self.save()
        return (self.dia, self.covid, self.sintomas)

