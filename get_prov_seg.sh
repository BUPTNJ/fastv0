
#judge if href_list exist
if [ ! -e "href_list" ]; then
    ./get_href_list.sh > href_list
fi

prov_name=$1

city_names=`cat href_list | grep $prov_name |gawk '{print $1}'`
for city_name in $city_names 
do
    file_name=./seg/"$city_name"_seg
    if [ ! -e $file_name ]; then
        ./get_city_seg.sh $city_name > $file_name
    fi
done