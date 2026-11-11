precio_unitario = 15.99
cantidad_a_comprar = 4

subtotal = precio_unitario * cantidad_a_comprar
descuento = subtotal * 0.1
total_final = subtotal - descuento
iva = total_final * 0.21

print ("subtotal", subtotal, "$")
print ("descuento", descuento, "$")
print ("total_final", total_final, "$")
print ("iva", iva, "$")