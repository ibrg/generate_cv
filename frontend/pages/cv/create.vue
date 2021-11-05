<template>
  <div>
    <div>
      <Row :space="10">
        <Cell
          v-for="n in 12"
          :key="n"
          :xs="24"
          :sm="12"
          :md="8"
          :lg="4"
          :xl="2"
        >
          <div>{{ n }}</div>
        </Cell>
      </Row>
    </div>
    <Row :space="2">
      <h1>Create</h1>
      <br>
      <form action="">
        <input v-model="cv.title" name="title" class="form-control" type="text" placeholder="Название">
        <input v-model="cv.fullname" name="fullname" class="form-control" type="text" placeholder="Фамилия и имя">
        <input v-model="cv.email" name="email" class="form-control" type="email" placeholder="Email">
        <input v-model="cv.contact" name="contact" class="form-control" type="text" placeholder="Контакт">
        <input v-model="cv.skills" name="skills" class="form-control" type="text" placeholder="Навыки">

        <select v-model="cv.english">
          <option value="" selected disabled hidden>
            Choose english level
          </option>
          <option v-for="option in ENGLISH_LEVEL" :key="option.value" :value="option.value">
            {{ option.text }}
          </option>
        </select>
        <br>
        <button @click.prevent="addWorkForm">
          Add Work
        </button>
        <span v-if="count > 0">
          <div v-for="(work, index) in cv.work_experience" :key="index">
            <input v-model="work.company_name" placeholder="Компания">
            <button @click.prevent="removeWorkForm(index)">Remove</button>
          </div>
        </span>

        <br>
        <input type="submit" value="Save" class="btn" @click.prevent="SubmitFrom">
      </form>
      <div class="">
        <pre>{{ count }}</pre>
        <pre>{{ cv }}</pre>
      </div>
    </Row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      count: 0,
      ENGLISH_LEVEL: [
        { value: '0', text: 'Не знаю' },
        { value: 'a1', text: 'A1 - Начальный уровень' },
        { value: 'a2', text: 'A2 - Элементарный уровень' },
        { value: 'b1', text: 'B1 - Средний уровень' },
        { value: 'b2', text: 'B2 - Средне-продвинутый уровень' },
        { value: 'c1', text: 'C1 - Продвинутый уровень' },
        { value: 'c2', text: 'C2 - Владение в совершенств' }
      ],
      cv: {
        title: '',
        fullname: '',
        email: '',
        contact: '',
        english: '',
        skills: '',
        work_experience: []
      }
    }
  },
  methods: {
    addWorkForm () {
      this.count++
      this.cv.work_experience.push({ company_name: '' })
    },
    removeWorkForm (index) {
      this.count--
      this.cv.work_experience.splice(index, 1)
    },
    SubmitFrom () {
      this.createCV()
      this.cv.title = ''
      this.cv.fullname = ''
      this.cv.email = ''
      this.cv.contact = ''
      this.cv.english = ''
      this.cv.skills = ''
      this.cv.work_experience = [{ company_name: '' }]
    },
    createCV () {
      this.$store.dispatch('createCV', {
        title: this.cv.title,
        fullname: this.cv.fullname,
        email: this.cv.email,
        contact: this.cv.contact,
        english: this.cv.english,
        skills: this.cv.skills,
        work_experience: this.cv.work_experience
      })
    }
  }
}
</script>
