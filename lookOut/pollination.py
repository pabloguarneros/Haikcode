for flower in bee.field_of_view:
    if flower.surface_charge_density < -0.4:
        e_field = generate_electric_field(bee, flower)
        if e_field.strength > 4:
            bee.pollinates(flower)