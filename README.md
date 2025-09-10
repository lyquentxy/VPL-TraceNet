# Vp2scratch

Toolkit to transform custom / Hour of Code / Karel / Visual Programming style AST or trace data into a Scratch 3.0–like `project.json` blocks structure.

## Project Layout

```
├── blocks/            # Block processing steps (id generation, opcode mapping, relationships, inputs, fields)
├── blocks_process.py  # Pipeline orchestration
├── tree2scr.py        # AST -> Scratch-like project entry
├── main.py            # Batch conversion example
├── config.py          # Central path configuration (env override)
├── scripts/           # One-off data prep / analytics utilities
├── tests/             # Basic smoke tests
├── requirements.txt   # Dependencies
```

## Quick Start

1. Prepare a dataset directory containing an `asts/` subfolder.
2. Set environment variable (PowerShell example):
   ```powershell
   $env:HOC_DATASET_PATH="E:/dataset/anonymizeddata/data/hoc18"
   ```
3. Run conversion:
   ```powershell
   python main.py
   ```
4. Generated Scratch-like JSON appears under `<DATASET>/scripts`.

## Configuration

`HOC_DATASET_PATH` points to the dataset root; default is local `./data`. Expected optional subfolders:

```
asts/          # Source AST JSON files
scripts/       # Generated output
trajectories/  # Trace text files (used by scripts/hourofcode.py etc.)
nextProblem/   # Mapping files (attemptSet, perfectSet, idMap, c2v_nextproblem.txt)
```

## Logging

The toolkit now just uses Python's standard library logging in `main.py` (basicConfig). Helper scripts print simple status lines; customize as needed.

## Extending

Add or modify opcode mappings in `blocks/set_opcode.py`. For large mappings consider loading from a JSON/YAML file prior to calling `map_opcodes`.

## Testing

Run tests:

```powershell
pytest -q
```

Add more cases under `tests/` for new language constructs.

## Roadmap

- External mapping configuration
- Input AST schema validation
- CLI flags (limit, verbose, output dir)
- Parallel processing

## Contributing

PRs welcome. Keep changes modular and add tests for new behavior.

## License

Add a LICENSE file (MIT / Apache-2.0 etc.).
