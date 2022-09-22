package program;
import java.util.ArrayList;

import cliente.PessoaFisica;
import cliente.PessoaJuridica;

public class Main {

	public static void main(String[] args) {
		
		ArrayList<PessoaFisica> pessoa01 = new ArrayList<PessoaFisica>();
		
		Empacotador empac = new Empacotador();
		
		empac.gravarArquivoBinario(pessoa01, "Arquivo_01");
		empac.lerArquivoBinario("Arquivo_01");
	}

}
