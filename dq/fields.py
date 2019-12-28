from django.db.models import BooleanField, CharField

'''
cilj class UniqueBooleanFieldTrue(BooleanField) je da kad se isactive polje stavi TRUE za neku dozvolu,
    onda da se za sve ostale dozvole automatski podesava FALSE,
    tako da postoji samo jedna aktivna dozvola ZA SVAKOG VOZACA.
    Medjutim, ovim class-om se samo jedna dozvola (ona za koju se rucno unosi isactive polje) stavlja u TRUE, dok se
    SVE OSTALE DOZVOLE, ZA SVE VOZACE stavljaju u FALSE
'''


class UniqueBooleanFieldTrue(BooleanField):
    def pre_save(self, model_instance, add):
        objects = model_instance.__class__.objects
        # If True then set all others as False
        if getattr(model_instance, self.attname):
            objects.update(**{self.attname: False})
        # If no true object exists that isnt saved model, save as True
        elif not objects.exclude(id=model_instance.id)\
                        .filter(**{self.attname: True}):
            return True
        return getattr(model_instance, self.attname)


class UniqueCharFieldActive(CharField):
    def pre_save(self, model_instance, add):
        objects = model_instance.__class__.objects
        # If True then set all others as False
        if getattr(model_instance, self.attname):
            objects.update(**{self.attname: 'Surrendered'})
        # If no true object exists that isnt saved model, save as True
        elif not objects.exclude(id=model_instance.id)\
                        .filter(**{self.attname: 'Active'}):
            return True
        return getattr(model_instance, self.attname)
