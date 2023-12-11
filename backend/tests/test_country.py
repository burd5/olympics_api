from api.models.country import Country
from settings import DATABASE, USER

def test_create_country_instance():
    attrs = ['Germany', 'GER']
    country = Country(attrs)

    assert isinstance(country, Country)

def test_find_all_athletes_for_country():
    attrs = ['Cambodia', 'CAM']
    country = Country(attrs)
    athletes = country.find_all_athletes_for_country()

    assert athletes == [{"id": 19700, "name": "Chan Seyha"}, {"id": 20607, "name": "Chhay-Kheng Nhem"}, {"id": 21179, "name": "Chov Sotheara"}, {"id": 31802, "name": "Ek Sam An"}, {"id": 38380, "name": "Isoup Ganthy"}, {"id": 47503, "name": "Hem Bunting"}, {"id": 47504, "name": "Hem Kiry"}, {"id": 47505, "name": "Hem Lumphat"}, {"id": 47506, "name": "Hem Reaksmey"}, {"id": 47508, "name": "Hem Thon Ponloeu"}, {"id": 47509, "name": "Hem Thon Vitiny"}, {"id": 58951, "name": "Ket Sivan"}, {"id": 59285, "name": "Khem Son"}, {"id": 59304, "name": "Khiru Soeun"}, {"id": 59363, "name": "Khom Ratanakmony"}, {"id": 59623, "name": "Kieng Samorn"}, {"id": 72579, "name": "Nary Ly"}, {"id": 78008, "name": "Meas Kheng"}, {"id": 90098, "name": "Ouk Chanthan"}, {"id": 94522, "name": "Phouk Sopheak"}, {"id": 96525, "name": "Sovijja Pou"}, {"id": 100113, "name": "Ret Chhon"}, {"id": 104384, "name": "Saing Pen"}, {"id": 105002, "name": "Samnang Prak"}, {"id": 105027, "name": "Samphon Mao"}, {"id": 105888, "name": "Sarun Van"}, {"id": 106261, "name": "Savin Chem"}, {"id": 111437, "name": "Sitha Sin"}, {"id": 112782, "name": "Sokhon Yi"}, {"id": 113260, "name": "Sorn Davin"}, {"id": 113261, "name": "Sorn Seavmey"}, {"id": 113337, "name": "Soth Sun"}, {"id": 113391, "name": "Sou Tit Linda"}, {"id": 118061, "name": "Kuniaki Takizaki"}, {"id": 118287, "name": "Tan Thol"}, {"id": 120367, "name": "Tim Phivana"}, {"id": 120613, "name": "To Rithya"}, {"id": 121445, "name": "Touch Kim Sy"}, {"id": 121446, "name": "Touch Nol"}, {"id": 124132, "name": "Van Son"}, {"id": 125514, "name": "Vath Chamroeun"}, {"id": 132958, "name": "Yi Yuong"}, {"id": 133173, "name": "You Chin Hong"}]