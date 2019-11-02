#!/usr/bin/env bash

auth=$( cat ./auth )

mkdir -p ./res

main() {
    cmd="curl --proxy socks5://127.0.0.1:1080 'https://icpc.baylor.edu/cm5-common-rest/rest/common/institutionunit/suggest?name=$1&page=0&size=10000' -H 'Pragma: no-cache' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' -H 'Accept: application/json' -H 'Referer: https://icpc.baylor.edu/private/profile/404758' -H 'Authorization: $auth' -H 'Connection: keep-alive' -H 'Cache-Control: no-cache' --compressed"
}

search() {
    res=$( eval ${cmd} )
    jud=$( echo ${res} | grep -i error )

    if [[ ${jud} == '' ]]; then
        echo ${res} > ./res/'result'$1'.txt'
        echo ${res}
    else
        exit 1
    fi
}

dict=(a b c d e f g h i j k l m n o p q r s t u v w x y z)
for xx in ${dict[@]}; do
    main
    search ${xx}&
done
