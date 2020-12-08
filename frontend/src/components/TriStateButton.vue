<template>
  <div>
    <span
      ref="input"
      class="checkbox"
      @click="clicked"
    />
    <span
      ref="label"
      class="label"
    />
  </div>
</template>

<script>
export default {
  name: "TriStateButton",
  props: {
    // Labels for TRUE, FALSE, NEUTRAL
    labels: {
      type: Array,
      default: () => ["True", "False", "Neutral"]
    },
    callback: {
      type: Function,
      default: (val, id) => {
      }
    },
    id: {
      type: String,
      default: ""
    },
    // eslint-disable-next-line vue/require-prop-types
    initial: {
      default: null
    },
  },
  data: function () {
    return {};
  },
  mounted() {
    this.setState(this.initial, this.$refs.input);
  },
  methods: {
    clicked: function () {
      let elem = this.$refs.input;

      if (elem.classList.contains('positive')) {
        this.setState(false, elem);
        this.callback(this.id, false);
      } else if (elem.classList.contains('negative')) {
        this.setState(null, elem);
        this.callback(this.id, null);
      } else {
        this.setState(true, elem);
        this.callback(this.id, true);
      }
    },
    setState(state, elem){
      if (state === true) {
        elem.classList.remove('negative');
        elem.classList.add('positive');
        elem.innerHTML = '<svg id="i-checkmark" viewBox="0 0 32 32" width="20" height="20" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="10.9375%"><path d="M2 20 L12 28 30 4" /></svg>';
        this.$refs.label.textContent = this.labels[0];
      } else if (state === false) {
        elem.classList.remove('positive');
        elem.classList.add('negative');
        elem.innerHTML = '<svg id="i-close" viewBox="0 0 32 32" width="20" height="20" fill="none" stroke="currentcolor" stroke-linecap="round" stroke-linejoin="round" stroke-width="10.9375%"><path d="M2 30 L30 2 M30 30 L2 2" /></svg>';
        this.$refs.label.textContent = this.labels[1];
      } else {
        elem.classList.remove('negative');
        elem.classList.remove('positive');
        elem.innerHTML = '';
        this.$refs.label.textContent = this.labels[2];
      }
    }
  }
}
</script>

<style scoped>
.checkbox {
  background-color: #fff;
  border: solid 1px #d7d7d7;
  border-radius: 4px;
  cursor: pointer;
  display: inline-block;
  height: 32px;
  margin-right: 1rem;
  text-align: center;
  width: 32px;
  vertical-align: middle;
}

.checkbox.svg {
  margin-top: 6px;
  stroke: #fff;
}

.positive {
  background-color: #4aca65;
  border-color: #43b45b;
}

.negative {
  background-color: #dc4e4e;
  border-color: #c74545;
}

.label {
  font-weight: bold;
  vertical-align: middle;
}
</style>