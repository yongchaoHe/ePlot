#!/bin/bash

# Colors
# Ref : https://www.cnblogs.com/lr-ting/archive/2013/02/28/2936792.html
color_black="\033[1;30m"
color_red="\033[1;31m"
color_green="\033[1;32m"
color_yellow="\033[1;33m"
color_blue="\033[1;34m"
color_purple="\033[1;35m"
color_skyblue="\033[1;36m"
color_white="\033[1;37m"
color_reset="\033[0m"

back_black="\033[40m"
back_red="\033[41m"
back_green="\033[42m"
back_yellow="\033[43m"
back_blue="\033[44m"
back_purple="\033[45m"
back_skyblue="\033[46m"
back_white="\033[47m"

echo_back() {
    cmdLog=${1}
    printf "[${color_purple}EXEC${color_reset}] ${cmdLog}\n"
    eval ${cmdLog}
}

echo_info() {
    cmdLog=${1}
    printf "[${color_green}INFO${color_reset}] ${cmdLog}\n"
}

echo_warn() {
    cmdLog=${1}
    printf "[${color_yellow}WARN${color_reset}] ${cmdLog}\n"
}

echo_erro() {
    cmdLog=${1}
    printf "[${color_red}ERRO${color_reset}] ${cmdLog}\n"
}

##
# Generate a split line
#
# @para 1
#   Length of the split line, (Optional)
# @para 2
#   synbol, (Optional)
# @para 3
#   Header, (Optional)
##
echo_line() {
    local _length=${1}
    local _symbol=${2}
    local _header=${3}

    if [ ! ${_length} ]; then
        _length=80
    fi
    if [ ! ${_symbol} ]; then
        _symbol="-"
    fi
    if [ $# -lt 3 ]; then
        printf "[${color_green}INFO${color_reset}] "
        for loop in `seq 1 ${_length}`
        do
            printf "${_symbol}"
        done
        printf "\n"
    else
        local _lenstr=${#_header}
        if [ ${_lenstr} -ge ${_length} ]; then
            _length=${_lenstr}
        fi
        local _lensym=$((_length-_lenstr))
        local _left=$((_lensym >> 1))
        local _right=$((_lensym - _left))
        printf "[${color_green}INFO${color_reset}] "
        for loop in `seq 2 ${_left}`
        do
            printf "${_symbol}"
        done
        printf " ${color_green}${_header}${color_reset} "
        for loop in `seq 2 ${_right}`
        do
            printf "${_symbol}"
        done
        printf "\n"
    fi
}

mkdir_if_not_exist() {
    local newdirFile=${1}
    if [ ! ${newdirFile} ]; then
        echo_erro "${FUNCNAME} argument is nil!"
        exit 0
    fi
    if [ ! -d ${newdirFile} ]; then
        echo_back "mkdir ${newdirFile}"
    fi
}

rmdir_if_exist() {
    local newdirFile=${1}
    if [ ! ${newdirFile} ]; then
        echo_erro "${FUNCNAME}: argument is nil!"
        exit 0
    fi
    if [ -d ${newdirFile} ]; then
        echo_back "rm -rf ${newdirFile}"
    fi
}

touch_if_not_exist() {
    local newFile=${1}
    if [ ! ${newFile} ]; then
        echo_erro "${FUNCNAME}: argument is nil!"
        exit 0
    fi
    if [ ! -f ${newFile} ]; then
        echo_back "touch ${newFile}"
    fi
}

rm_if_exist() {
    local newFile=${1}
    if [ ! ${newFile} ]; then
        echo_erro "${FUNCNAME}: argument is nil!"
        exit 0
    fi
    if [ -f ${newFile} ]; then
        echo_back "rm ${newFile}"
    fi
}

################################################################
pycmd=python
################################################################

show_usage() {
    local appname=$0
    echo_info "Usage: ${appname} {build | install | clean}"
    exit 0
}

build() {
    # Generate binary distributions
    echo_back "${pycmd} setup.py bdist" 
}

install() {
    echo_back "sudo ${pycmd} setup.py install" 
}

clean() {
    rmdir_if_exist "build"
    rmdir_if_exist "dist"
    rmdir_if_exist "ePlot.egg-info"
}

################################################################
####################    * Main Process *    ####################
################################################################
export LC_ALL=C

if (( $# == 0 )); then
    show_usage
    exit 0
fi

if (( $UID == 0 )); then
    echo_warn "Don't run this script as root"
    exit 0
fi

global_choice=${1}
case ${global_choice} in
    "build")
        build 
        ;;
    "install")
        install 
        ;;
    "clean")
        clean
        ;;
    *)
        show_usage
        ;;
esac
