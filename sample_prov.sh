prov_name=$1
./get_prov_seg.sh $prov_name
city_names=`cat href_list | grep $prov_name |gawk '{print $1}'`
for city_name in $city_names 
do
    seg_name=./seg/"$city_name"_seg
    sample_name=./sample/"$city_name"_sample
    if [ ! -e $sample_name ]; then
        ./sample_city.sh $city_name > $sample_name
    fi
done