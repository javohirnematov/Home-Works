nalogi = float(0.12)
chayeviye = float(0.18)

zakaz_na_summu = float(input('Заказ на сумму в ресторане $: '))
summa_naloga = zakaz_na_summu * nalogi
print('Cумма налога $%.2f.'% summa_naloga)
summa_chayevix = zakaz_na_summu * chayeviye
print('Cумма чаевых $%.2f.'% summa_chayevix)
obshiy_chek = zakaz_na_summu + summa_naloga + summa_chayevix
print('Чек в ресторане на сумму $%.2f.'% obshiy_chek)
