import click
from synthetic_data_toolkit.synthetic import SyntheticDataGenerator

@click.group()
def cli():
    """Synthetic Data Toolkit CLI"""
    pass

@cli.command()
@click.option('--prompt', '-p', required=True, help='The prompt to generate synthetic data from.')
@click.option('--output', '-o', default='synthetic_data.txt', help='The output file to save the generated synthetic data.')
@click.option('--max-tokens', '-m', default=1000, help='The maximum number of tokens to generate.')
@click.option('--temperature', '-t', default=0.7, help='The temperature for generation (0.0 to 1.0).')
def generate(prompt, output, max_tokens, temperature):
    """Generate synthetic data based on a prompt."""
    generator = SyntheticDataGenerator()
    click.echo("Generating synthetic data...")
    result = generator.generate(prompt, max_tokens=max_tokens, temperature=temperature)
    
    if result:
        with open(output, 'w') as f:
            f.write(result)
        click.echo(f"Synthetic data saved to {output}")
    else:
        click.echo("Failed to generate synthetic data.")

if __name__ == '__main__':
    cli()