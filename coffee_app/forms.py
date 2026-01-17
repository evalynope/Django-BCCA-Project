from django import forms
from .models import BrewEntry
from .models import Roast
from django import forms
from .models import BrewEntry


class BrewEntryForm(forms.ModelForm):
    class Meta: 
        model = BrewEntry
        fields = [
            "title",
            "roast",
            "brew_method",
            "entry",
            "rating",
        ]
        widgets = {
            "entry": forms.Textarea(attrs={"rows": 4}), 
        }

    def clean(self):
        cleaned_data = super().clean()
        brew_method = cleaned_data.get("brew_method")
        other_method = cleaned_data.get("other_brew_method")
        title = cleaned_data.get("title").strip()
        entry = cleaned_data.get("entry").strip()

      
        if title and title.isdigit():
             self.add_error(
            "title",
            "Title cannot only be numeric. Please provide character values."
        )
        
        entry_compact = entry.replace(" ", "").replace("\n", "")
        if entry_compact.isdigit():
             self.add_error(
                "entry",
                "Entry cannot only be numeric. Please provide character values."
            )
        

        return cleaned_data



from django import forms
from .models import Roast

class RoastForm(forms.ModelForm): 
    class Meta:
        model = Roast
        fields = [
            "coffee_shop",
            "name",
            "origin",
            "tasting_notes",
            "profile",
            "crowd",
            "is_seasonal",
            "is_available",
            "is_good_to_gift",
        ]

        widgets = {
            "tasting_notes": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Flavor notes, aroma..."
            }),
        }
