CREATE TABLE transfer AS 
    SELECT 
        id, 
        LOWER(marca) AS marca,
        LOWER(modelo) AS modelo,
        LOWER(mod) AS mod,
        LOWER(body_type) AS body_type,
        LOWER(portas) AS portas,
        LOWER(bancos) AS bancos,
        LOWER(bagagem) AS bagagem,
        LOWER(combustivel) AS combustivel,
        LOWER(sistema_combustivel) AS sistema_combustivel,
        LOWER(tipo_motor) AS tipo_motor,
        LOWER(posicao_motor) AS posicao_motor,
        LOWER(capacidade_motor) AS capacidade_motor,
        LOWER(cylinders) AS cylinders,
        LOWER(power_out) AS power_out,
        LOWER(aceleracao) AS aceleracao,
        LOWER(velocidade_max) AS velocidade_max,
        LOWER(rodas_motrizes) AS rodas_motrizes,
        LOWER(tipo_direcao) AS tipo_direcao,
        LOWER(gear_box) AS gear_box,
        LOWER(comprimento) AS comprimento,
        LOWER(largura) AS largura,
        LOWER(altura) AS altura,
        LOWER(peso) AS peso,
        LOWER(wheel_base) AS wheel_base,
        LOWER(suspensao_frontal) AS suspencao_frontal,
        LOWER(suspensao_traseira) AS suspencao_traseira,
        LOWER(freios_frontais) AS freios_frontais,
        LOWER(freios_traseiros) AS freios_traseiros,
        LOWER(pneus_dianteiros) AS pneus_frontais,
        LOWER(pneus_traseiros) AS pneus_traseiros,
        LOWER(fuel_urban) AS fuel_urban,
        LOWER(fuel_extra_urban) AS fuel_extra_urban,
        LOWER(fuel_combined) AS fuel_combined,
        LOWER(volume_tanque) AS volume_tanque,
        img 
    FROM cars;
