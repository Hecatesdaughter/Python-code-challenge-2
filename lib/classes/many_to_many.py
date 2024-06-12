class Band:
    def __init__(self, name, hometown):
        self._name = None
        self._hometown = None
        self.name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def hometown(self):
        return self._hometown
    
    def __setattr__(self, attr, value):
        if hasattr(self, attr) and attr == 'hometown':
            raise AttributeError("Cannot change hometown once set")
        super().__setattr__(attr, value)

    def add_concert(self, concert):
        if isinstance(concert, Concert):
            self._concerts.append(concert)
        else:
            raise ValueError("Concert must be an instance of Concert")

    @property
    def concerts(self):
        return self._concerts if self._concerts else None

    @property
    def venues(self):
        if not self._concerts:
            return None
        
        unique_venues = set()
        for concert in self._concerts:
            unique_venues.add(concert.venue)

        return list(unique_venues)

    def play_in_venue(self, venue, date):
        new_concert = Concert(date, self, venue)
        self.add_concert(new_concert)
        return new_concert

    def all_introductions(self):
        if not self._concerts:
            return None
        
        introductions = []
        for concert in self._concerts:
            introduction = f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            introductions.append(introduction)
        
        return introductions

class Venue:
    def __init__(self, name, city):
        self._name = None
        self._city = None
        self.name = name
        self.city = city
        self._concerts = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string")
    
    def add_concert(self, concert):
        if isinstance(concert, Concert):
            self._concerts.append(concert)
        else:
            raise ValueError("Concert must be an instance of Concert")

    def concerts(self):
        return self._concerts if self._concerts else None

    def bands(self):
        if not self._concerts:
            return None
        
        unique_bands = set()
        for concert in self._concerts:
            unique_bands.add(concert.band)

        return list(unique_bands)

        
class Concert:
    def __init__(self, date, band, venue):
        self._date = None
        self._band = None
        self._venue = None
        self.date = date
        self.band = band
        self.venue = venue

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string")

    @property
    def band(self):
        return self._band
    
    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError("Band must be an instance of Band")

    @property
    def venue(self):
        return self._venue
    
    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError("Venue must be an instance of Venue")

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
