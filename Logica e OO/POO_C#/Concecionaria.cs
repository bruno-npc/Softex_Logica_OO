
namespace ConcecioCar
{
    public class Concecionaria
    {
        private string modelo;
        private int ano;
        private float potencia;

        public Concecionaria(string modelo, int ano, float potencia){
            this.modelo = modelo;
            this.ano = ano;
            this.potencia = potencia;
        }
        public Concecionaria(){}

        void setModelo(string modelo) {this.modelo = modelo;}
        string getModelo() {return this.modelo;}

        void setAno(int ano) {this.ano = ano;}
        int getAno() {return this.ano;}

        void setPotencia(float potencia) {this.potencia = potencia;}
        float getPotencia() {return this.potencia;}

    }
}