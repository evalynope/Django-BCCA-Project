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
    
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if not title or not title.strip():
            raise forms.ValidationError("Title cannot be blank.")
        if title.strip().isdigit():
            raise forms.ValidationError(
                "Title cannot only be numeric. Please provide character values."
            )
        return title.strip()
    
    def clean_entry(self):
        entry = self.cleaned_data.get("entry")
        if not entry or not entry.strip():
            raise forms.ValidationError("Entry cannot be blank.")

        entry_compact = entry.replace(" ", "").replace("\n", "")
        if entry_compact.isdigit():
            raise forms.ValidationError(
                "Entry cannot only be numeric. Please provide character values."
            )

        return entry.strip()
            
        # entry_compact = entry.replace(" ", "").replace("\n", "")
        # if entry_compact.isdigit():
        #      self.add_error(
        #         "entry",
        #         "Entry cannot only be numeric. Please provide character values."
        #     )  
             
        # return cleaned_data
        
    
    # def clean_entry(self):
    #     entry = self.cleaned_data.get("entry") or ''
    #     if not entry or not entry.strip():
    #         raise forms.ValidationError("Entry cannot be blank")
    #     return entry
        

    

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
