import os
import time
import json
from datetime import datetime
import subprocess
import random  # For demo purposes, replace with actual measurements

class VDBenchCore:
    def __init__(self):
        self.results_file = "results.json"
        self._load_results()
        
    def _load_results(self):
        if os.path.exists(self.results_file):
            with open(self.results_file, "r") as f:
                self.results = json.load(f)
        else:
            self.results = []
            
    def _save_results(self, new_result):
        self.results.append(new_result)
        with open(self.results_file, "w") as f:
            json.dump(self.results, f)
            
    def run_benchmark(self, test_type, block_size, threads, duration, target_path):
        """
        Generator function that yields progress updates during the benchmark
        """
        start_time = time.time()
        
        # Validate target path
        if not os.path.exists(target_path):
            raise ValueError(f"Target path {target_path} does not exist")
            
        # Convert block size to bytes
        block_size_bytes = self._parse_block_size(block_size)
        
        # Initialize test file if needed
        test_file = os.path.join(target_path, "vdbench_test_file")
        self._prepare_test_file(test_file, block_size_bytes)
        
        elapsed_time = 0
        while elapsed_time < duration:
            # In a real implementation, these would be actual measurements
            # This is just for demonstration
            progress = {
                'percent': (elapsed_time / duration),
                'status': 'Running benchmark...',
                'iops': random.uniform(1000, 100000),
                'throughput': random.uniform(100, 2000),
                'latency': random.uniform(0.1, 10)
            }
            
            yield progress
            
            time.sleep(1)
            elapsed_time = time.time() - start_time
            
        # Save final results
        final_result = {
            'timestamp': datetime.now().isoformat(),
            'test_type': test_type,
            'block_size': block_size,
            'threads': threads,
            'duration': duration,
            'iops': progress['iops'],
            'throughput': progress['throughput'],
            'latency': progress['latency']
        }
        
        self._save_results(final_result)
        
    def _parse_block_size(self, block_size):
        """Convert block size string (e.g., '4K') to bytes"""
        units = {'K': 1024, 'M': 1024*1024}
        size = int(block_size[:-1])
        unit = block_size[-1]
        return size * units[unit]
        
    def _prepare_test_file(self, file_path, block_size):
        """Prepare test file if it doesn't exist"""
        if not os.path.exists(file_path):
            # Create a test file of appropriate size (e.g., 1GB)
            subprocess.run(['dd', 'if=/dev/zero', f'of={file_path}',
                          'bs=1M', 'count=1024']) 