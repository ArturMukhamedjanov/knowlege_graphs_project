import json
import random

def generate_winrate_data(agents_file, maps_file, ranks_file, output_file):
    # Загрузка данных из файлов
    with open(agents_file, 'r', encoding='utf-8') as f:
        agents = json.load(f)
        
    with open(maps_file, 'r', encoding='utf-8') as f:
        maps = json.load(f)
        
    with open(ranks_file, 'r', encoding='utf-8') as f:
        ranks = json.load(f)
    
    # Получаем только номера рангов
    rank_numbers = ranks.values()

    data = []
    
    # Генерация записей для каждого агента, карты и ранга
    for agent in agents:
        for other_agent in agents:
            if agent == other_agent:
                continue  # Исключаем комбинацию агента с самим собой
            for map_name in maps:
                for rank in rank_numbers:
                    winrate = round(random.uniform(35, 65), 2)  # Генерация винрейта от 35 до 65
                    record = {
                        "name": agent,
                        "withAgent": other_agent,
                        "winrate": winrate,
                        "map": map_name,
                        "rank": rank
                    }
                    data.append(record)
    
    # Сохранение данных в файл
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Данные успешно сгенерированы и сохранены в файл: {output_file}")

# Пути к файлам
generate_winrate_data(
    agents_file="data/agents.json",
    maps_file="data/maps.json",
    ranks_file="data/ranks.json",
    output_file="winrate_with_data.json"
)
