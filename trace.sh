src_name=$1
prov_name=$2
./sample_prov $prov_name
city_names=`cat href_list | grep $prov_name |gawk '{print $1}'`
for city_name in $city_names 
do
    file_name="$src_name"_trace/"$src_name"_trace_$city_name
    if [ ! -e $file_name ]; then
        scamper -f ./sample/"$city_name"_sample > $file_name
    fi
done