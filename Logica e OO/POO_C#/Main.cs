using System;
using static ConcecioCar.Concecionaria;
class Main {
    static void main(string[] args) 
    {
        Concecionaria carro1 = new Concecionaria();

        carro1.setModelo("teste1");
        carro1.setAno(2021);
        carro1.setPotencia(80);

        carro1.getAno();
        carro1.getPotencia();
        carro1.getModelo();

    }
}