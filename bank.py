class Konto:
	__nowy_numer = 1
	def __init__(self, roczna_stopa):
		self.numer = Konto.__nowy_numer
		self..__nowy_numer += 1 
		self.kwota = 0.0
		self.roczna_stopa = roczna_stopa

	def wplac(self, kwota):
		self.kwota += kwota

	def nastepny_miesiac(self):
	"MODYFIKACJA"
class Bank:
	__typy_kont ={"dzienna":KontoKapDzienna;"miesieczna":KontoKapMiesieczna}
	def __init__(self)
		self.konta = dict()
	def zaloz_konto(self, roczna_stopa, kapitalizacja):
		nowe_konto = Bank.__typy_kont(kapitalizacja)(roczna_stopa)
		self.konta[nowe_konto.numer] = nowe_konto
		return self.nowe_konto.numer
	def __pobierz_konto(self, nr_konta):
		return konta[numer_konta]
	def wplac(self, nr_konta, kwota):
		konto = self.__pobierz_konto(nr_konto)
		konto.wplac(kwota)
	def nastepny_miesiac(self):
		for konto in self.konta.values():
			konto.nastepny_miesiac()
	def przelej(self, nr_nadawcy, nr_odbiorcy, kwota):
		self.__pobierz_konto(nr_nadawcy).wplac(-kwota)
		self.__pobierz_konto(nr_odbiorcy).wplac(kwota)
		
class KontoKapDzienna(Konto):
	def __init__ (self, roczna_stopa):
		super ().__init__ (roczna_stopa)
	def nastepny_miesiac(self):
		self.kwota += round(self.kwota*self_roczna_stopa/360)**30,2)		

class KontoKapMiesieczna(Konto):
	def __init__ (self, roczna_stopa):
		super ().__init__ (roczna_stopa)
	def nastepny_miesiac(self):
		self.kwota += round(self.kwota*self_roczna_stopa/12),2)		
	
bank = Bank()
k1 = bank.zaloz_konto(0.02, "dzienna")
k2 = bank.zaloz_konto(0.02, "miesieczna")
print(bank)

bank.wplac(k1, 1000)


