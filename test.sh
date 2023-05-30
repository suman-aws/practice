values="m1 m2 m3"
converted_values=$(echo "$values" | sed 's/ /,/g')
echo "$converted_values"
