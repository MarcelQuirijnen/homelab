package main

import (
	"fmt"
	"goBlockChain/src/wallet"
	"log"
)

func init() {
	log.SetPrefix("BlockChain: ")
}

func main() {
	w := wallet.NewWallet()
	fmt.Println(w.PrivateKeyStr())
	fmt.Println(w.PublicKeyStr())
}
