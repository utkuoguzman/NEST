import nest

print("--- Standard NEST CPU Hello World ---")
nest.ResetKernel()
nest.SetKernelStatus({"resolution": 0.1})

# Create a neuron and a spike generator
neuron = nest.Create("iaf_psc_alpha")
spike_gen = nest.Create("spike_generator", params={"spike_times": [10.0, 50.0]})
voltmeter = nest.Create("voltmeter")

# Connect them
nest.Connect(spike_gen, neuron, syn_spec={"weight": 500.0})
nest.Connect(voltmeter, neuron)

# Simulate
print("Simulating for 100 ms...")
nest.Simulate(100.0)

# Extract and print results
events = voltmeter.get("events")
if "times" in events and len(events["times"]) > 0:
    print(f"Recorded times: {events['times'][:5]} ...")
    print(f"Recorded potentials: {events['V_m'][:5]} ...")

print("Standard NEST Hello World successful!")

