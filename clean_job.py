def clean_function(context, path):
    import os
    import time
    from pathlib import Path

    base_root = Path(path)
    now = time.time()
    age_limit = 1 * 24 * 60 * 60

    for uuid_dir in base_root.iterdir():
        snapshots_dir = uuid_dir / "snapshots"
        if snapshots_dir.is_dir():
            for file in snapshots_dir.iterdir():
                try:
                    if file.is_file():
                        mtime = file.stat().st_mtime
                        if now - mtime > age_limit:
                            file.unlink()
                            print(f"Deleted: {file}")
                except Exception as e:
                    print(f"Error deleting {file}: {e}")

