#!/usr/bin/env bash

main() {
  if [ $(expr $1 % 3) == 0 ]; then
    echo -n "Pling"
  fi
  if [ $(expr $1 % 5) == 0 ]; then
    echo -n "Plang"
  fi
  if [ $(expr $1 % 7) == 0 ]; then
    echo -n "Plong"
  fi
  if [ $(expr $1 % 3) != 0 ] && [ $(expr $1 % 5) != 0 ] && [ $(expr $1 % 7) != 0 ]; then
    echo $1
  fi

}

main "$@"
