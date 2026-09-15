import nestgpu as ngpu

print("--- NEST-GPU Hello World ---")

# Create a neuron
neuron = ngpu.Create("iaf_psc_alpha")

# Create a record instead of a voltmeter
record = ngpu.CreateRecord("", ["V_m_rel"], [neuron[0]], [0])

# Simulate
print("Simulating for 100 ms on GPU...")
ngpu.Simulate(100.0)

print("NEST-GPU Hello World successful!")
